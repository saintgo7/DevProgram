// Add Impulse

#include "Program064.h"

AProgram064::AProgram064()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram064::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Add Impulse ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating add impulse."));

    // Implement the program logic here...
}

void AProgram064::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
