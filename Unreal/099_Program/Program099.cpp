// Game Instance Subsystem

#include "Program099.h"

AProgram099::AProgram099()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram099::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Game Instance Subsystem ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating game instance subsystem."));

    // Implement the program logic here...
}

void AProgram099::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
