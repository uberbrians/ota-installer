from dataclasses import dataclass, field
from pathlib import Path


import build.tasks as tasks
import build.variables as variables


@dataclass
class PayloadImageRenamer(tasks.TaskFactoryTemplate):
    instance: type[variables.Manager] = field(default=variables.Manager)

    @property
    def index(self) -> int:
        return 2

    @property
    def title(self) -> str:
        return "Payload Image Renamer"

    @property
    def command_string(self) -> str:
        source_path = Path.home().joinpath("payload.bin")
        destination_path = Path.home().joinpath(
            self.instance.boot_image_struct.payload.file_name
        )

        return f"mv -v {source_path} {destination_path}"
