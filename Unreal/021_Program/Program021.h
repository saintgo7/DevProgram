// Blueprint Callable
// Program 021

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program021.generated.h"

UCLASS()
class AProgram021 : public AActor
{
    GENERATED_BODY()

public:
    AProgram021();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
