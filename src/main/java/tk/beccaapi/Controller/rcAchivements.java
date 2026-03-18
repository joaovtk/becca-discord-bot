package tk.beccaapi.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import tk.beccaapi.Model.Achivements;
import tk.beccaapi.Model.AchivementsUser;
import tk.beccaapi.Model.User;
import tk.beccaapi.Model.Repo.AchivementsRepo;
import tk.beccaapi.Model.Repo.AchivementsUserRepo;
import tk.beccaapi.Model.Repo.UserRepo;

@RequestMapping("/achivements")
@RestController
public class rcAchivements {

    @Autowired
    public UserRepo userRepo;
    @Autowired
    public AchivementsRepo achivRepo;
    @Autowired
    public AchivementsUserRepo achivUserRepo;

    
    @GetMapping("/gain")
    public String getGain(@RequestParam String userId, @RequestParam() String achivId, @RequestParam() String achivCmd){
        User fetch = userRepo.findByUserId(userId);
        String msg = "";
        if(fetch == null){
            User user = new User(userId, 10.0, 0.0);
            userRepo.save(user);
            Achivements fetchAchiv = achivRepo.findByAchivId(achivId);
            if (fetchAchiv == null){
                msg = "Essa conquista ainda não existe";
            }  
        }else {
            // Pegar o usuario e comparar se ele possui a conquista
            AchivementsUser achivment = achivUserRepo.findOne(String userId);
            
            if(achivment != null){
                msg = "Not passed";
            }else {
                AchivementsUser achivement = new AchivementsUser(achivId, userId, achivCmd);
                achivUserRepo.save(achivement);
                msg = "Respect";
            }
        }
        return msg;
    }

    @GetMapping("/add")
    public String getAdd(@RequestParam() String achivId, @RequestParam() String achivCmd, @RequestParam() String desc){
        String msg = "";
        Achivements fetchAchiv = achivRepo.findByAchivId(achivId);
        if(fetchAchiv == null){
            Achivements newAchiv = new Achivements(achivId, msg, achivCmd, desc);
            achivRepo.save(newAchiv);
            msg = "Conquista adicionada";
        }else {
            msg = "Conquista já existe";
        }
        return msg;
    
    }
}
