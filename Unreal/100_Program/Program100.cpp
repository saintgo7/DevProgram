// Local Player Subsystem

#include "Program100.h"

AProgram100::AProgram100()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram100::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Local Player Subsystem ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating local player subsystem."));

    // Implement the program logic here...
}

void AProgram100::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
