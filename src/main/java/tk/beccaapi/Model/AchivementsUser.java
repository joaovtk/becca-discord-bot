package tk.beccaapi.Model;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class AchivementsUser {
    private String achivId;
    private String userId;
    private String achivCmd;

    public AchivementsUser(String achivId, String userId, String achivCmd){
        this.achivId = achivId;
        this.userId = userId;
        this.achivCmd = achivCmd;
    }
}
