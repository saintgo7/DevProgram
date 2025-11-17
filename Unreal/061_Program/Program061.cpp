// Physics

#include "Program061.h"

AProgram061::AProgram061()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram061::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Physics ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating physics."));

    // Implement the program logic here...
}

void AProgram061::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
