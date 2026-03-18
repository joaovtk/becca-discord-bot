package tk.beccaapi.Model.Repo;

import org.springframework.data.mongodb.repository.MongoRepository;

import tk.beccaapi.Model.AchivementsUser;
import java.util.List;



public interface AchivementsUserRepo extends MongoRepository<AchivementsUser, String>{
    List<AchivementsUser> findByAchivCmd(String achivCmd);
    AchivementsUser findByAchivId(String achivId);
    List<AchivementsUser> findByUserId(String userId);
}
