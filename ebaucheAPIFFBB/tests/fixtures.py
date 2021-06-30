from typing import Optional, List

from django.contrib.auth.models import User, Group

from ebaucheAPIFFBB.ffbbapi.models import Place, Member


def create_app_user(
        username: str,
        password: Optional[str] = None,
        first_name: Optional[str] = "first name",
        last_name: Optional[str] = "last name",
        email: Optional[str] = "foo@bar.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
        groups: List[Group] = [],
) -> User:
    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_staff=is_staff,
        is_superuser=is_superuser,
        is_active=is_active,
    )
    return user


def place_factory():
    def create_place(
            code="111111111111111",
            latitude=47.273576,
            longitude=-2.213869,
            title="endroit",
            address="rue de la vie",
            post_code="44600",
            city="Saint-Nazaire"
    ) -> Place:
        place = Member.objects.create(
            code=code,
            latitude=latitude,
            longitude=longitude,
            title=title,
            address=address,
            post_code=post_code,
            city=city
        )
        return place

    return create_place()


def member_factory(place: Place):
    def create_member(
            first_name="test",
            last_name="test_last",
            phone="0123456789",
            email="test@test.com",
            address=place
    ) -> Member:
        member = Member.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            address=place
        )
        return member

    return create_member()
