package hello;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class HelloContorller {
    @RequestMapping("/")
    public String index() {
        return "Hello, World!";
    }
}
