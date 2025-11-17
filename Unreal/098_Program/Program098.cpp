// World Subsystem

#include "Program098.h"

AProgram098::AProgram098()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram098::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== World Subsystem ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating world subsystem."));

    // Implement the program logic here...
}

void AProgram098::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
