// Hello World
// Program 001

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program001.generated.h"

UCLASS()
class AProgram001 : public AActor
{
    GENERATED_BODY()

public:
    AProgram001();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
