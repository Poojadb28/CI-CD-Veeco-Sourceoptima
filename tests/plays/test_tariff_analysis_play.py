import pytest
import os


@pytest.mark.regression
def test_tariff_analysis_play(tariff_analysis_play):

    tariff = tariff_analysis_play

    download_dir = os.path.abspath("downloads")
    os.makedirs(download_dir, exist_ok=True)

    # ================= EXPORT BOM =================
    tariff.export_bom(download_dir)

    # ================= APPROVE BOM =================
    tariff.approve_bom()

    #================= Complete HTS Wizard =================
    tariff.complete_hts_wizard()

    tariff.wait_for_processing_complete()

    # ================= EXPORT TARIFF =================
    tariff.export_tariff(download_dir)

    # ================= BACK =================
    tariff.go_back()