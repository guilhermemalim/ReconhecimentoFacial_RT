import java.util.List;
import java.awt.image.BufferedImage;

public interface ModelProvider {
    // retorna a lista de usuários reconhecidos
    // se for um único usuário, retorna uma lista com 1 elemento
    public List<String> getInference(BufferedImage image);
}