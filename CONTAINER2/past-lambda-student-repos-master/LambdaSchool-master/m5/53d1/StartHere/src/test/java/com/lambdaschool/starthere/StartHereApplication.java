package com.lambdaschool.starthere;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.core.env.Environment;
import org.springframework.web.servlet.DispatcherServlet;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

@EnableWebMvc
// @EnableJpaAuditing
@SpringBootApplication
public class StartHereApplication {
    private static final Logger logger = LoggerFactory.getLogger(com.lambdaschool.starthere.StartHereApplication.class);
    private static boolean stop = false;

    @Autowired
    private static Environment env;

    private static void checkEnvironmentVariable(String envvar) {
        if (System.getenv(envvar) == null) {
            logger.error("Environment Variable " + envvar + " missing");
            stop = true;
        }
    }

    public static void main(String[] args) {
        checkEnvironmentVariable("OAUTHCLIENTID");
        checkEnvironmentVariable("OAUTHCLIENTSECRET");

        if (!stop) {
            ApplicationContext ctx = SpringApplication.run(com.lambdaschool.starthere.StartHereApplication.class,
                                                           args);

            DispatcherServlet dispatcherServlet = (DispatcherServlet) ctx.getBean("dispatcherServlet");
            dispatcherServlet.setThrowExceptionIfNoHandlerFound(true);
        }
    }

}
