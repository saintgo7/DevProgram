// Sublevel

#include "Program059.h"

AProgram059::AProgram059()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram059::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Sublevel ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating sublevel."));

    // Implement the program logic here...
}

void AProgram059::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
