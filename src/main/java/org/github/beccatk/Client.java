package org.github.beccatk;

import io.github.cdimascio.dotenv.Dotenv;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.OnlineStatus;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.events.ReadyEvent;
import net.dv8tion.jda.api.interactions.commands.OptionType;
import net.dv8tion.jda.api.interactions.commands.build.Commands;
import net.dv8tion.jda.api.interactions.commands.build.SubcommandData;
import net.dv8tion.jda.api.interactions.commands.build.SubcommandGroupData;
import net.dv8tion.jda.api.requests.GatewayIntent;
import net.dv8tion.jda.api.requests.restaction.CommandListUpdateAction;
import org.github.beccatk.Events.ReadyEventListener;
import org.github.beccatk.Events.SlashCommandListener;

import java.util.EnumSet;

public class Client {

    private String token;
    private JDABuilder jda;
    public Client(String token){
        this.token = token;
        this.jda = JDABuilder.createDefault(this.token, EnumSet.of(GatewayIntent.GUILD_MEMBERS, GatewayIntent.GUILD_MESSAGE_TYPING, GatewayIntent.MESSAGE_CONTENT, GatewayIntent.GUILD_VOICE_STATES, GatewayIntent.GUILD_EMOJIS_AND_STICKERS));
    }

    public void start(){
        this.jda.addEventListeners(new ReadyEventListener());
        this.jda.addEventListeners(new SlashCommandListener());

        this.jda.setActivity(Activity.playing("Estou de volta em java"));

        SubcommandGroupData[] data = {
                new SubcommandGroupData("ação", "Comandos de açoes")
                    .addSubcommands(
                            new SubcommandData("abraçar", "Abraça a pessoa mencionada").addOption(OptionType.USER, "usuario", "O usuario que você quer abraçar"),
                            new SubcommandData("beijar", "Beija a pessoa mencionada").addOption(OptionType.USER, "usuario", "O usuario que você quer beijar"),
                            new SubcommandData("bater", "Dá um tapa na pessoa mencionada").addOption(OptionType.USER, "usuario", "O usuario que você quer estapear")
                    ),

                new SubcommandGroupData("utilidades", "Comandos de utilidades").addSubcommands(
                        new SubcommandData("clima", "Mostra o clima da sua cidade").addOption(OptionType.STRING, "cidade", "Nome da cidade"),
                        new SubcommandData("urban", "Pesquisa no dicionario girias").addOption(OptionType.STRING, "giria", "A giria que você quer pesquisar"),
                        new SubcommandData("citação", "Gera uma citação aleatoria"),
                        new SubcommandData("horóscopo", "Dá uma previsão de horóscopo para o signo informado").addOption(OptionType.STRING, "signo", "Seu signo")
                ),

                new SubcommandGroupData("quiz", "Comandos de quiz").addSubcommands(
                        new SubcommandData("enviar", "Enviar um quiz para analisamos, você deve preencher todas informaçoes abaixo"),
                        new SubcommandData("começar", "Começa a partida do quiz"),
                        new SubcommandData("parar", "Encerra uma partida do quiz"),
                        new SubcommandData("topserv", "Mostra as pessoas com mais ponto no servidor, e sua posição"),
                        new SubcommandData("topglobal", "Mostra as 10 pessoas com mais pontos no bot, e sua posição")
                )

        };

        SubcommandData[] funnySub = {new SubcommandData("dado", "Rola um dado de 0 a 10, você escolhe o limite de lados").addOption(OptionType.NUMBER, "limite", "limite do numero de dados"),
                new SubcommandData("8ball", "Bola 8 ou 8ball é um jogo você uma pergunta e eu respondo se você deve ou não fazer ou que eu acho").addOption(OptionType.STRING, "question", "Uma pergunta aleatoria que você quer fazer"),
                new SubcommandData("meme", "Gera um meme aleatorio"),
                new SubcommandData("piada", "Gera uma piada aleatoria"),
                new SubcommandData("gato", "Envia para você uma foto de gato aleatoria para alegrar seu dia"),
                new SubcommandData("zombar", "Gera uma frase totalmente distorcida que você enviou").addOption(OptionType.STRING, "mensagem", "Mensagem que você quer distorcer"),
                new SubcommandData("ship", "Medi o amor que você tem com pessoa selecionada").addOption(OptionType.USER, "usuario", "A pessoa amada que você quer saber seu nivel de paixão"),
                new SubcommandData("guerra", " Inicia uma batalha com um outro usuário").addOption(OptionType.USER, "usuario", "O usuario que você quer travar uma guerra"),
                new SubcommandData("avatar", "Mostra a foto de outra pessoa").addOption(OptionType.USER, "usuario", "O usuario que você quer ver a foto"),
                new SubcommandData("sorte", "Pega um cookie da sorte para você ler (isso custa 1 cookie da sua carteira)"),
                new SubcommandData("coinflip", "Tira cara ou coroa"),
                new SubcommandData("banf", "Executa um ban falso na pessoa, caso você queria dar um susto"),
                new SubcommandData("pokemon", "Quem é esse pokemon, caso acerte ganhar (15 cookies)"),
                new SubcommandData("fatos", "Gera um fato aleatorio, isso deveria estar em um short do youtube"),
                new SubcommandData("comida", "Gera uma foto de comida aleatoria"),
                new SubcommandData("filme", "Eu recomendo um filme para você assistir")

        };

        CommandListUpdateAction commands = this.jda.build().updateCommands();
        commands.addCommands(
                Commands.slash("ping", "Faz a bot falar pong"),
                Commands.slash("funny", "Comandos focados em diversão")
                        .addSubcommands(funnySub)
                        .addSubcommandGroups(data),
                Commands.slash("rpg", "Comandos de rpg")

        );
        commands.queue();
    }
}
