package tk.beccaapi.Model;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class User {
    private String userId;
    private double rupes;
    private double xp;
    private int cookies;

    public User(String userId, double rupes, double xp, int cookies){
        this.userId = userId;
        this.xp = xp;
        this.rupes = rupes;
        this.cookies = cookies;
    }

    public void incCookies(int cookies){
        this.cookies += cookies;
    }

    public void incRupes(double rupes){
        this.rupes += rupes;
    }

    public void removeRupes(double rupes){
        this.rupes -= rupes;
    }
}
