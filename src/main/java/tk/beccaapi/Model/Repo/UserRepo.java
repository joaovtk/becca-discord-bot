package tk.beccaapi.Model.Repo;

import org.springframework.data.mongodb.repository.MongoRepository;

import tk.beccaapi.Model.User;


public interface UserRepo extends MongoRepository<User, String>{
    User findByUserId(String userId);
}
