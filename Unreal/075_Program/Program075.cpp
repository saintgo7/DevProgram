// Particle Spawn

#include "Program075.h"

AProgram075::AProgram075()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram075::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Particle Spawn ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating particle spawn."));

    // Implement the program logic here...
}

void AProgram075::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
