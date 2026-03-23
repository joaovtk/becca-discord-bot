package tk.beccaapi.Model.Repo;

import org.springframework.data.mongodb.repository.MongoRepository;

import tk.beccaapi.Model.Achievements;

import java.util.List;


public interface AchievementsRepo extends MongoRepository<Achievements, String>{
    Achievements findByIdentifier(String identifier);
    List<Achievements> findByIdentifierCommand(String indentifierCommand);
}
