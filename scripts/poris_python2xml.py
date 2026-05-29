import argparse
import importlib.util
import sys
from contextlib import redirect_stdout
from pathlib import Path


def load_model_class(model_file: Path, class_name: str | None):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "PORIS"))
    sys.path.insert(0, str(model_file.resolve().parent))

    module_name = model_file.stem
    spec = importlib.util.spec_from_file_location(module_name, model_file)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load Python model from {model_file}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if class_name is None:
        class_name = module_file_to_class_name(model_file)

    try:
        return getattr(module, class_name)
    except AttributeError as exc:
        raise RuntimeError(f"Class {class_name} not found in {model_file}") from exc


def module_file_to_class_name(model_file: Path) -> str:
    stem = model_file.stem
    return stem if stem.endswith("PORIS") else f"{stem}PORIS"


def main():
    parser = argparse.ArgumentParser(description="Generate PORIS XML from a generated Python PORIS model")
    parser.add_argument("model_file", type=Path, help="generated *PORIS.py file")
    parser.add_argument("-o", "--output", type=Path, help="output XML file")
    parser.add_argument("--class-name", help="PORISDoc subclass name; defaults to the file stem")
    parser.add_argument("--project-id", type=int, default=0)
    args = parser.parse_args()

    model_file = args.model_file.resolve()
    output_file = args.output
    if output_file is None:
        output_file = model_file.with_suffix(".xml")

    model_class = load_model_class(model_file, args.class_name)
    model = model_class(args.project_id)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("wb") as xml_fp:
        with redirect_stdout(sys.stderr):
            xml_doc = model.toXML()
        xml_fp.write(xml_doc.toprettyxml(indent="    ", encoding="UTF-8"))

    print(output_file)


if __name__ == "__main__":
    main()
