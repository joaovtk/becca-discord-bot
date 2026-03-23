package tk.beccaapi.Model.Repo;

import org.springframework.data.mongodb.repository.MongoRepository;
import tk.beccaapi.Model.AchievementsUser;
import java.util.List;



public interface AchievementsUserRepo extends MongoRepository<AchievementsUser, String>{
    List<AchievementsUser> findByIdentifierCommand(String identifierCommand);
    AchievementsUser findByIdentifier(String identifier);
    List<AchievementsUser> findByUserId(String userId);
    AchievementsUser findByUserIdAndIdentifier(String userId, String identifier);
}
