import pytest
from autodistill.detection import CaptionOntology

from autodistill_grounded_sam_2.grounded_sam_2 import GroundedSAM2


@pytest.fixture
def video_path():
    return "asset/palace.mp4"


@pytest.fixture
def grounded_sam_client():
    ontology = CaptionOntology(
        {
            "person": "person",
        }
    )
    grounding_dino_box_threshold = 0.35
    grounding_dino_text_threshold = 0.25
    video_mode = True
    sam2_grounded = GroundedSAM2(
        ontology,
        "Grounding DINO",
        grounding_dino_box_threshold,
        grounding_dino_text_threshold,
        video_mode,
    )
    return sam2_grounded


def test_video_sam(video_path, grounded_sam_client):
    detection = grounded_sam_client.predict(video_path)

    assert detection.mask is not None
    assert detection.class_id is not None
    assert detection.confidence is not None
    assert detection.tracker_id is not None
    assert detection.xyxy is not None
    assert detection.xyxy.shape[0] > 0
    assert detection.mask.shape[0] > 0
    assert detection.class_id.shape[0] > 0
    assert detection.confidence.shape[0] > 0
    assert detection.tracker_id.shape[0] > 0
