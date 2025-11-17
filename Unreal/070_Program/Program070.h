// Normal Map
// Program 070

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program070.generated.h"

UCLASS()
class AProgram070 : public AActor
{
    GENERATED_BODY()

public:
    AProgram070();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
