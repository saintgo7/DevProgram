// Blueprint Callable

#include "Program021.h"

AProgram021::AProgram021()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram021::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Blueprint Callable ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating blueprint callable."));

    // Implement the program logic here...
}

void AProgram021::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
