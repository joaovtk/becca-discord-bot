package org.github.beccatk.Events;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class SlashCommandListener extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(SlashCommandInteractionEvent event){
        if(event.getName().equals("ping")){
            event.deferReply();

            EmbedBuilder[] embeds = {new EmbedBuilder().setColor(0x00ff00)
                    .setTitle("PONG!!!!")
                    .setDescription("Eu sei que esse comando tem em todo bot, mas é porque ele é padrão...")
                    .setAuthor("Melhor Mesa Tenista ou jogadora de ping pong do java", "https://github.com/joaovtk/becca-discord-bot")
            };
            event.reply("").addEmbeds(embeds[0].build()).queue();
        }
    }
}
