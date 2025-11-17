// Capsule Collision

#include "Program014.h"

AProgram014::AProgram014()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram014::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Capsule Collision ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating capsule collision."));

    // Implement the program logic here...
}

void AProgram014::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
