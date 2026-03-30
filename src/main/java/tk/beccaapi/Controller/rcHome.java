package tk.beccaapi.Controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@RequestMapping("/")
public class rcHome {
    @GetMapping()
    public String invalidUrl(){
        return "Check docs for endpoints return";
    }
}
