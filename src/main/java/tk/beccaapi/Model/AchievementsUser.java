package tk.beccaapi.Model;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class AchievementsUser {
    private String identifier;
    private String userId;
    private String identifierCommand;

    public AchievementsUser(String identifier, String userId, String identifierCommand){
        this.identifier = identifier;
        this.userId = userId;
        this.identifierCommand = identifierCommand;
    }
}
