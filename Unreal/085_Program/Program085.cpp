// Camera Manager

#include "Program085.h"

AProgram085::AProgram085()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram085::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Camera Manager ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating camera manager."));

    // Implement the program logic here...
}

void AProgram085::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
