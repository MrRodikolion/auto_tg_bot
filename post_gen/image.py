import PIL.Image
from imaginairy.api import imagine, imagine_image_files
from imaginairy.schema import ImaginePrompt, WeightedPrompt, LazyLoadingImage, ControlInput
from imaginairy.utils.log_utils import configure_logging

configure_logging()


def gen_img(ans) -> PIL.Image.Image:
    prompts = [
        ImaginePrompt(f'{ans}', steps=20),
    ]

    for result in imagine(prompts):
        return result.img

