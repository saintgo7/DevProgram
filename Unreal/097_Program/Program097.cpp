// Subsystem

#include "Program097.h"

AProgram097::AProgram097()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram097::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Subsystem ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating subsystem."));

    // Implement the program logic here...
}

void AProgram097::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
