package tk.beccaapi.Model.Repo;

import org.springframework.data.mongodb.repository.MongoRepository;

import tk.beccaapi.Model.Achivements;

import java.util.List;


public interface AchivementsRepo extends MongoRepository<Achivements, String>{
    Achivements findByAchivId(String achivId);
    List<Achivements> findByAchivCmd(String achivCmd);
}
