package tk.beccaapi.Model;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class User {
    private String userId;
    private double yen;
    private double xp;

    public User(String userId, double yen, double xp){
        this.userId = userId;
        this.xp = xp;
        this.yen = yen;
    }
}
