package tk.beccaapi.Model;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class Achivements {
    private String achivId;
    private String achivCmd;
    private String desc;

    public Achivements(String achivId, String userId, String achivCmd, String desc){
        this.achivId = achivId;
        this.achivCmd = achivCmd;
        this.desc = desc;
    }
}
