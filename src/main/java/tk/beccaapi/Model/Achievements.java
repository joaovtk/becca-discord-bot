package tk.beccaapi.Model;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class Achievements {
    private String identifier;
    private String identifierCommand;
    private String desc;

    public Achievements(String identifier, String identifierCommand, String desc){
        this.identifier = identifier;
        this.identifierCommand = identifierCommand;
        this.desc = desc;
    }
}
