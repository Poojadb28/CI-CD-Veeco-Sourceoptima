import pytest
import os


@pytest.mark.regression
def test_tariff_analysis_play(tariff_analysis_play):

    tariff = tariff_analysis_play

    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    # ================= EXPORT BOM =================
    tariff.export_bom(download_dir)

    # Validate BOM file downloaded
    bom_files = [
        f for f in os.listdir(download_dir)
        if f.endswith(".xlsx") and not f.endswith(".crdownload")
    ]

    assert len(bom_files) > 0, "BOM file not downloaded"

    for file in bom_files:
        path = os.path.join(download_dir, file)
        assert os.path.getsize(path) > 0, f"{file} is empty"

    # ================= APPROVE BOM =================
    tariff.approve_bom()

    # ================= COMPLETE HTS WIZARD =================
    tariff.complete_hts_wizard()
    tariff.wait_for_processing_complete()

    # ================= EXPORT TARIFF =================
    tariff.export_tariff(download_dir)

    # Validate Tariff file downloaded
    tariff_files = [
        f for f in os.listdir(download_dir)
        if "tariff" in f.lower() and f.endswith(".xlsx")
    ]

    assert len(tariff_files) > 0, "Tariff file not downloaded"

    for file in tariff_files:
        path = os.path.join(download_dir, file)
        assert os.path.getsize(path) > 0, f"{file} is empty"

    # ================= BACK =================
    tariff.go_back()

