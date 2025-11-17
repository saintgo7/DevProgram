// World Composition

#include "Program060.h"

AProgram060::AProgram060()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram060::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== World Composition ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating world composition."));

    // Implement the program logic here...
}

void AProgram060::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
