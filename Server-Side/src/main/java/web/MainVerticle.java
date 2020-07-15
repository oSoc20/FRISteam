package web;

import io.vertx.core.AbstractVerticle;
import io.vertx.core.AsyncResult;
import io.vertx.core.Promise;
import io.vertx.core.http.HttpMethod;
import io.vertx.core.http.HttpServer;
import io.vertx.ext.web.Router;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.handler.BodyHandler;
import io.vertx.ext.web.handler.CorsHandler;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Class to set up Vertx for http server
 *
 * {@link AbstractVerticle}
 */
public class MainVerticle extends AbstractVerticle {
    private static final String HTTP_PORT = "http.port";
    private static final int HTTP_FALLBACK_PORT = 8001;
    private static final Logger LOGGER = Logger.getLogger(MainVerticle.class.getSimpleName());
    private ApiEndPoint apiEndPoint = new ApiEndPoint();

    /**
     *  Start the verticle instance.
     *
     * @param startPromise a future.
     * {@link AbstractVerticle#start(Promise)}
     */
    @Override
    public void start(Promise<Void> startPromise){
        vertx.createHttpServer()
                .requestHandler(buildRoutes(enableCors()))
                .listen(config().getInteger(HTTP_PORT, HTTP_FALLBACK_PORT), asyncResult -> listener(asyncResult, startPromise));
    }

    /**
     * Builds the routes for the http server and handles 500 errors.
     *
     * @param router a router
     * @return the built router
     */
    private Router buildRoutes(final Router router) {
        apiEndPoint.installRoutes(router);
        router.errorHandler(500, this::handle500Error);
        return router;
    }

    /**
     * Handler for 500 errors.
     *
     * @param routingContext a {@link RoutingContext}
     */
    private void handle500Error(RoutingContext routingContext) {
        LOGGER.log(Level.SEVERE, "Internal Server Error", routingContext.failure());
    }

    /**
     * Sets the CORS for the requests
     *
     * @return a {@link Router}
     */
    private Router enableCors() {
        Router router = Router.router(vertx);
        router.route().handler(CorsHandler.create(".*.")
                .allowedHeader("x-requested-with")
                .allowedHeader("Access-Control-Allow-Origin")
                .allowedHeader("origin")
                .allowedHeader("Content-Type")
                .allowedHeader("accept")
                .allowedMethod(HttpMethod.GET)
                .allowedMethod(HttpMethod.POST)
                .allowedMethod(HttpMethod.DELETE)
                .allowedMethod(HttpMethod.PUT));
        router.route().handler(BodyHandler.create());
        return router;
    }

    /**
     * The listener for async responses
     *
     * @param res a response
     * @param startPromise a promise
     */
    private void listener(final AsyncResult<HttpServer> res, Promise<Void> startPromise) {
        if (res.succeeded()){
            startPromise.complete();
            LOGGER.info(()-> String.format("Server is listening on port: %s", res.result().actualPort()));
        }
        else {
            startPromise.fail("Failed to start http server");
            LOGGER.info(() -> String.format("Failed to bind on port: %s", config()
                    .getInteger(HTTP_PORT, HTTP_FALLBACK_PORT)));
        }
    }
}
