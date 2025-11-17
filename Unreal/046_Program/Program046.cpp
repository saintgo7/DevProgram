// Widget Blueprint

#include "Program046.h"

AProgram046::AProgram046()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram046::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Widget Blueprint ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating widget blueprint."));

    // Implement the program logic here...
}

void AProgram046::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
