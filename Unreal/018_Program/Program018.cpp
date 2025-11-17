// USceneComponent

#include "Program018.h"

AProgram018::AProgram018()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram018::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== USceneComponent ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating uscenecomponent."));

    // Implement the program logic here...
}

void AProgram018::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
