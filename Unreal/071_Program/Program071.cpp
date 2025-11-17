// Particle System

#include "Program071.h"

AProgram071::AProgram071()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram071::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Particle System ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating particle system."));

    // Implement the program logic here...
}

void AProgram071::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
