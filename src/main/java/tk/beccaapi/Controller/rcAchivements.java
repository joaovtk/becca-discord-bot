package tk.beccaapi.Controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import tk.beccaapi.Controller.dto.AddRequest;
import tk.beccaapi.Controller.dto.GainRequest;
import tk.beccaapi.Controller.dto.Response;
import tk.beccaapi.Model.Achievements;
import tk.beccaapi.Model.AchievementsUser;
import tk.beccaapi.Model.User;
import tk.beccaapi.Model.Repo.AchievementsRepo;
import tk.beccaapi.Model.Repo.AchievementsUserRepo;
import tk.beccaapi.Model.Repo.UserRepo;

@RequestMapping("/achievements")
@RestController
public class rcAchivements {
    @Autowired
    private UserRepo userRepo;
    @Autowired
    private AchievementsRepo achievementsRepo;
    @Autowired
    private AchievementsUserRepo achievementsUserRepo;
    
    @Value("${SECRET}")
    private String secret;

    @PostMapping("/gain")
    public ResponseEntity<Response> getGain(@RequestBody GainRequest request){
        if(request.secret().equals(secret)){
            User fetch = userRepo.findByUserId(request.userId());
            ResponseEntity<Response> msg;
            if(fetch == null){
                User user = new User(request.userId(), 10.0, 0.0, 0);
                userRepo.save(user);
            }
            
            Achievements fetchAchievements = achievementsRepo.findByIdentifier(request.identifier());
            if(fetchAchievements == null){
                msg = ResponseEntity.status(403).body(new Response("Essa conquista não existe", "403"));
            }else {
                AchievementsUser achievementsUser = achievementsUserRepo.findByUserIdAndIdentifier(request.userId(), request.identifier());
                if(achievementsUser == null){
                    AchievementsUser newAchievementsUser = new AchievementsUser(request.identifier(), request.userId(), fetchAchievements.getIdentifierCommand());
                    achievementsUserRepo.save(newAchievementsUser);
                    userRepo.findByUserId(request.userId()).incCookies(request.cookies());
                    userRepo.findByUserId(request.userId()).incRupes(request.rupes());;
                    msg = ResponseEntity.status(200).body(new Response("Conquista registrada", "200"));
                }else {
                    msg = ResponseEntity.status(403).body(new Response("Você já tem conquista", "403"));
                }
            }
            return msg;
        }else {
            ResponseEntity<Response> msg;
            msg = ResponseEntity.status(401).body(new Response("Forbiden", "403"));
            return msg;
        }
    }

    @PostMapping("/add")
    public ResponseEntity<Response> getAdd(@RequestBody AddRequest request){
        if(request.secret().equals(secret)){
            ResponseEntity<Response> msg;
            Achievements fetchAchievements = achievementsRepo.findByIdentifier(request.identifier());
            if(fetchAchievements == null){
                Achievements newAchievements = new Achievements(request.identifier(), request.identifierCommand(), request.desc());
                achievementsRepo.save(newAchievements);
                msg = ResponseEntity.status(200).body(new Response("Conquista adicionada", "200"));
            }else {
                msg = ResponseEntity.status(403).body(new Response("Conquista já existe", "403"));
            }
            return msg;
        }else {
            ResponseEntity<Response> msg;
            msg = ResponseEntity.status(403).body(new Response("Você já tem conquista", "403"));
            return msg;
        }
    }
}
