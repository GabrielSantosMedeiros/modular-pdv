from configuration.settings import IMAGE_DIR
from pathlib import Path
import shutil
from database.models import Produto


class ProdutoService:

    def _save_image(self, image_path, new_name):
        IMAGE_DIR.mkdir(parents=True, exist_ok=True)
        extension = Path(image_path).suffix
        dir_path = IMAGE_DIR / f'{new_name}{extension}'

        shutil.copy(image_path, dir_path)


    def save(self, obj:Produto):
        obj.imagem = Path(obj.imagem).as_posix()
        obj.save(force_insert=True)
        self._save_image(obj.imagem, obj.nome)
        return obj.__json__()