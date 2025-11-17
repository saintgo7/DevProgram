// Collision Component

#include "Program011.h"

AProgram011::AProgram011()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram011::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Collision Component ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating collision component."));

    // Implement the program logic here...
}

void AProgram011::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
