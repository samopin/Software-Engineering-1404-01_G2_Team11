from __future__ import annotations

from typing import Dict

from ..models.destination_info import DestinationInfo
from ..ports.wiki_service_port import WikiServicePort


def _normalize_destination_name(destination_name: str | None) -> str:
    if destination_name is None:
        return ""
    return " ".join(destination_name.strip().split()).title()


class WikiClient(WikiServicePort):
    """Safe placeholder wiki client with internal fallback data."""

    _FALLBACK_DATA: Dict[str, DestinationInfo] = {
        "Tehran": DestinationInfo(
            name="Tehran",
            description="Capital city of Iran with a mix of modern life and historical landmarks.",
            country="Iran",
            region="Tehran Province",
        ),
        "Shiraz": DestinationInfo(
            name="Shiraz",
            description="Known for poetry, gardens, and historical attractions in southern Iran.",
            country="Iran",
            region="Fars Province",
        ),
        "Isfahan": DestinationInfo(
            name="Isfahan",
            description="Historic city famous for Persian architecture, bridges, and public squares.",
            country="Iran",
            region="Isfahan Province",
        ),
    }

    def get_destination_basic_info(self, destination_name: str) -> DestinationInfo:
        normalized_name = _normalize_destination_name(destination_name)
        if not normalized_name:
            return DestinationInfo(
                name="Unknown",
                description="No destination was provided.",
                country="Unknown",
                region="Unknown",
            )

        if normalized_name in self._FALLBACK_DATA:
            return self._FALLBACK_DATA[normalized_name]

        return DestinationInfo(
            name=normalized_name,
            description=f"Basic information for {normalized_name} is not available yet.",
            country="Unknown",
            region="Unknown",
        )


class MockWikiClient(WikiServicePort):
    """Deterministic in-memory mock for testing and local development."""

    _MOCK_DATA: Dict[str, DestinationInfo] = {
        "Tehran": DestinationInfo(
            name="Tehran",
            description="تهران پایتخت ایران است و مرکز اصلی سیاسی و اقتصادی کشور محسوب می‌شود.",
            country="Iran",
            region="Tehran Province",
        ),
        "Shiraz": DestinationInfo(
            name="Shiraz",
            description="شیراز به شعر فارسی، باغ‌ها و میراث فرهنگی غنی‌اش شناخته می‌شود.",
            country="Iran",
            region="Fars Province",
        ),
        "Isfahan": DestinationInfo(
            name="Isfahan",
            description="اصفهان به معماری دوره صفوی و میدان‌ها و بناهای تاریخی‌اش مشهور است.",
            country="Iran",
            region="Isfahan Province",
        ),
    }

    def get_destination_basic_info(self, destination_name: str) -> DestinationInfo:
        normalized_name = _normalize_destination_name(destination_name)
        if not normalized_name:
            return DestinationInfo(
                name="Unknown",
                description="پیش‌فرض ماک: مقصدی وارد نشده است.",
                country="Unknown",
                region="Unknown",
            )

        if normalized_name in self._MOCK_DATA:
            return self._MOCK_DATA[normalized_name]

        return DestinationInfo(
            name=normalized_name,
            description=f"اطلاعات پیش‌فرض ماک برای {normalized_name}.",
            country="Unknown",
            region="Unknown",
        )


def get_wiki_client(use_mock: bool = True) -> WikiServicePort:
    if use_mock:
        return MockWikiClient()
    return WikiClient()
