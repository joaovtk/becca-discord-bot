package org.github.beccatk;

import io.github.cdimascio.dotenv.Dotenv;

public class Main {

    public static void main(String[] args) {
        Dotenv dotenv = Dotenv.load();
        Client bot = new Client(dotenv.get("TOKEN"));
        bot.start();
    }
}