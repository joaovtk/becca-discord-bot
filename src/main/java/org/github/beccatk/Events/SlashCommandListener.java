package org.github.beccatk.Events;

import java.util.Random;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class SlashCommandListener extends ListenerAdapter {
    @Override
    public void onSlashCommandInteraction(SlashCommandInteractionEvent event){
        String commandName = event.getName();
        if(commandName.equals("pong")){
            event.deferReply();

            EmbedBuilder[] embeds = {new EmbedBuilder().setColor(0x00ff00)
                    .setTitle("PONG!!!!")
                    .setDescription("Eu sei que esse comando tem em todo bot, mas é porque ele é padrão...")
                    .setAuthor("Melhor Mesa Tenista ou jogadora de ping pong do java", "https://github.com/joaovtk/becca-discord-bot")
            };
            event.reply("").addEmbeds(embeds[0].build()).queue();
        }else if(event.getName().equals("funny")){
            String subName = event.getSubcommandName();
            if(subName.equals("8ball")){
                String[] responses = {
                    // Respostar positivas
                    "Isto é certo",
                    "Isto está decididamente certo",
                    "Sem dúvida",
                    "Sim, Definitivamente",
                    "Você pode confiar nisso",
                    "Pelo que vejo sim",
                    "Provavelmente",
                    "Pelo que vejo isso é bom",
                    "Sim...",
                    "Todos os sinais apontos que sim",
                    "A ajuda virá de uma fonte inesperada... tipo, REALMENTE inesperada.",
                    // Respostas Neutras
                    "Tente perguntar novamente",
                    "Melhor não te contar agora",
                    "Não posso prever agora",
                    "Desculpe. Ninguém está aqui agora para atender sua ligação. Deixe uma mensagem após o sinal",
                    // Respostas negativas
                    "Por favor, não conte com isso",
                    "Minha Resposta é não",
                    "Minhas fontes dizem que não",
                    "Pela minha experiencia, não",
                    "Má Ideia",
                    "*Chamo meu advogado*",
                    "Isso é uma pessima ideia",
                    "Você já tentou desligá-lo e ligá-lo novamente ?",
                    "Não, mas sei que você vai tentar de qualquer maneira, seu idiota.",
                    "Talvez, com grande força de vontade",
                    "Talvez com muita *Determinação*"
                };
                Random rand = new Random();
                EmbedBuilder[] embeds = {
                    new EmbedBuilder()
                    .setTitle("Sua pergunta foi " + (event.getOption("question").getAsString()))
                    .setDescription("Meu veredito foi decidido e **" + responses[rand.nextInt(responses.length)] + "**")
                    .setColor(0x0f0)
                    .setAuthor("Vidente pessoal da becca", "https://github.com/joaovtk/becca-discord-bot")
                };

                event.reply("").addEmbeds(embeds[0].build()).queue();
            }
        }
    }
}
