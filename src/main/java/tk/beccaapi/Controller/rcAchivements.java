package tk.beccaapi.Controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import tk.beccaapi.Controller.dto.Response;
import tk.beccaapi.Model.Achievements;
import tk.beccaapi.Model.AchievementsUser;
import tk.beccaapi.Model.User;
import tk.beccaapi.Model.Repo.AchievementsRepo;
import tk.beccaapi.Model.Repo.AchievementsUserRepo;
import tk.beccaapi.Model.Repo.UserRepo;

@RequestMapping("/achivements")
@RestController
public class rcAchivements {
    @Autowired
    private UserRepo userRepo;
    @Autowired
    private AchievementsRepo achievementsRepo;
    @Autowired
    private AchievementsUserRepo achievementsUserRepo;
    
    @GetMapping("/gain")
    public ResponseEntity<Response> getGain(@RequestParam String userId, @RequestParam() String identifier){
        User fetch = userRepo.findByUserId(userId);
        ResponseEntity<Response> msg;
        if(fetch == null){
            User user = new User(userId, 10.0, 0.0);
            userRepo.save(user);
           
        }
        
        Achievements fetchAchievements = achievementsRepo.findByIdentifier(identifier);
        if(fetchAchievements == null){
            msg = ResponseEntity.status(403).body(new Response("Essa conquista não existe", "403"));
        }else {
            AchievementsUser achievementsUser = achievementsUserRepo.findByUserIdAndIdentifier(userId, identifier);
            if(achievementsUser == null){
                AchievementsUser newAchievementsUser = new AchievementsUser(identifier, userId, fetchAchievements.getIdentifierCommand());
                achievementsUserRepo.save(newAchievementsUser);
                msg = ResponseEntity.status(200).body(new Response("Conquista registrada", "200"));
            }else {
                msg = ResponseEntity.status(403).body(new Response("Você já tem conquista", "403"));
            }
        }
        return msg;
    }

    @GetMapping("/add")
    public ResponseEntity<Response> getAdd(@RequestParam() String identifier, @RequestParam() String identifierCommand, @RequestParam() String desc){
        ResponseEntity<Response> msg;
        Achievements fetchAchievements = achievementsRepo.findByIdentifier(identifier);
        if(fetchAchievements == null){
            Achievements newAchievements = new Achievements(identifier, identifierCommand, desc);
            achievementsRepo.save(newAchievements);
            msg = ResponseEntity.status(403).body(new Response("Conquista adicionada", "403"));
        }else {
            msg = ResponseEntity.status(403).body(new Response("Conquista já existe", "403"));
        }
        return msg;
    }
}
