// Sound Attenuation
// Program 078

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program078.generated.h"

UCLASS()
class AProgram078 : public AActor
{
    GENERATED_BODY()

public:
    AProgram078();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
