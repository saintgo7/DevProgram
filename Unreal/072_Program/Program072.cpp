// Niagara

#include "Program072.h"

AProgram072::AProgram072()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram072::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Niagara ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating niagara."));

    // Implement the program logic here...
}

void AProgram072::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
